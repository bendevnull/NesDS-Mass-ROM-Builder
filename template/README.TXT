This is the stripped down version by Gericom orginally made for "7 GrandDadY". I've modified this slightly to allow quick embeds of new roms on compile.

Unused stuff like UI/Wifi have been removed and will auto boot a rom embedded into the SRL at compiled.

This will operate in both NTR mode and TWL mode. (TWL mode compatiblity available if compiled on devkitarm r46).

Note that fat libraries have been disabled and this does not support saves/save states. This is meant for things like DS Download Play and hardware where DLDI/SD is not available.

Release binaries will not be made available for this. You will need to provide your own roms and compile this yourself.

This will only boot a single rom. Put the game in arm9/data and rename to "rom.nes". Then compile using make.