# AIR-ENX

English translation mod for Nintendo Switch version of "Air" 1.0.1

---

Current status: **Alpha**

Chapters translation status:
- Dream 100%
- Summer 100%
- Air 100%
- 初空の章 (Hatsusora no Shou) 0%

To do:
- Replace images with translated text
- Translate 4th chapter (no translation exists on any platform)

Known issues:
- Plugin is required for translating most of settings texts, fixing date format and putting english warning text. It is known that plugins made with Skyline framework are not compatible with any emulator last time this repository was updated (it will result in emulator's crash). Do not use plugin if you are using emulator.
- Images containing Japanese text in scenario are not translated. But their translation can be seen in message logs when available after showing image(s).
- Any change to scenario file makes saves pointing to this scenario in most cases broken (trying to load it will result in going back to main menu). Main save data is not touched by this issue. If you are updating mod, be aware that your saves may not work anymore and you will need to skip through chapter's text to the point where you have ended.

Port of translation is based on patr0805's work with PSP English translation mod as they share similarities in how scenario was handled.
Their translation is based mostly on "Gao Gao Translations" work with tidbits from "Winter Confetti" translation.
Big thanks to all people involved with AIR translation.

Sources:</br>
https://patr0805.wordpress.com/2020/02/13/air-psp-first-release/ </br>
https://gaogaotranslation.wordpress.com/ </br>
https://winter-confetti.blogspot.com/2014/04/air-standard-edition-2005-english-patch.html </br>

---

# Making mod manually

Requirements:
- Python 3.10+ (and libraries: `numpy`, `PyPNG`)

If you want to use cmd files, you need:
- Windows 10+
- WSL Ubuntu

For plugin compilation you need:
- devkitpro (with `switch-dev` package installed)

Instructions: 
1. Download repo with all submodules
2. Extract `SCRIPT.PAK` and `image\PARTS.PAK` from romfs of game. You can use [NXDumpTool](https://github.com/DarkMatterCore/nxdumptool/releases) for that. Put those files to `PAKs` folder in downloaded repo,
3. Run `0.Unpack.cmd` without Administrator privileges,
4. Run `1.Replace_All.cmd` without Administrator privileges,
5. Run `2.Make_Script.cmd` without Administrator privileges,
6. (Optional) Run `3.Compile_Plugin.cmd` without Administrator privileges,
7. Copy `atmosphere` folder to the root of sdcard used in your Switch,
8. Run game.

# Installing mod from release
1. Download "MOD.zip"
2. (Optional - don't use it in emulator) Download "Plugin.zip"
3. Unpack both and copy `atmosphere` folder to the root of sdcard used in your Switch,
4. Run game

---

# Notes

- Main chapters that exists both in PSP and Switch version has scenario almost 1:1. Switch version has additional few lines in place where H-scenes in PC occur.
- Some texts were swapped in favor of "Winter Confetti" translation as their text felt more natural.
