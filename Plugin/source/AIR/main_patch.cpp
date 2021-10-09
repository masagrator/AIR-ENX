#include "skyline/inlinehook/And64InlineHook.hpp"
#include "skyline/utils/cpputils.hpp"
#include "AIR/JPN.hpp"
#include "AIR/ENG.hpp"
#include <vector>
#include <string>
#include <algorithm>

uintptr_t TextRegionOffset = 0;

uint64_t (*boot_original)(void* unk0);
uint64_t boot_hook(void* unk0) {
	std::u16string bootWarning = u"This is a work of fiction.\n"
	u"Any resemblance to actual people, locales, organizations, illnesses, or diseases is purely coincidental.";

	uintptr_t New_Warningptr = (uintptr_t)bootWarning.c_str();
	
	memcpy((void*)(TextRegionOffset + 0x2F8360), (void*)&New_Warningptr, 8);
	return boot_original(unk0);
}

uint64_t (*PrintDate_original)(void* unk0, const char* format, void* year, void* month, void* day);
uint64_t PrintDate_hook(void* unk0, const char* format, void* year, void* month, void* day){
	std::string new_format = "%02d/%02d/%04d";
	return PrintDate_original(unk0, new_format.c_str(), day, month, year);
}

void (*Parse_original)(void* unk1, const char* UTF8_string);
void Parse_hook(void* unk1, const char* UTF8_string)
{
	std::string check = UTF8_string;
	std::vector<std::string>::iterator itr = std::find(JPN.begin(), JPN.end(), check);
	if (itr != JPN.cend()) {
		Parse_original(unk1, ENG[std::distance(JPN.begin(), itr)].c_str());
	}
	else Parse_original(unk1, UTF8_string);
}

void air_main()
{
	TextRegionOffset = (uintptr_t)skyline::utils::getRegionAddress(skyline::utils::region::Text);
	//UI Text
	A64HookFunction((void*)(TextRegionOffset + 0x112F0),
			reinterpret_cast<void*>(Parse_hook),
			(void**)&Parse_original);
	//Print Date
		A64HookFunction((void*)(TextRegionOffset + 0x232920),
			reinterpret_cast<void*>(PrintDate_hook),
			(void**)&PrintDate_original);
	//Boot
		A64HookFunction((void*)(TextRegionOffset + 0x20D780),
			reinterpret_cast<void*>(boot_hook),
			(void**)&boot_original);	
}
