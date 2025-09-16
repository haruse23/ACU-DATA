Credits for gentlegiantJGC for the `decompress_.py` and `resources`

https://github.com/gentlegiantJGC/ACExplorer/blob/master/pyUbiForge/misc/decompress_.py

Decompression Python Code can run on AC1 if Chunk Count is read as 2 bytes instead of 4, like this:

`Chunk_Count = struct.unpack_from("<H", f.read(2), 0x00)[0]`

Same goes for the `ACU_DATA_Compressed.hexpat` file, this is a pattern file to be used in the Hex Editor `ImHex`, if you change Chunk Count from 4 bytes to 2 bytes it will work on AC1 Compressed `.data` files, like this:

`u32 CHUNK_Count;`

`FORGE.hexpat` can run on both ACU and AC1 without any changes

Other AC games are not tested yet, feel free to try with other games

`
