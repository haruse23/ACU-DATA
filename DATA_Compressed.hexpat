import std.core;
import std.mem;

struct CHUNK {
    u16 Uncompressed_Size;
    u16 Compressed_Size;
};

struct CHUNK_Data {
    u32 Hash;
    
    u64 i = std::core::array_index();
    u8 data[parent.chunk[i].Compressed_Size];
};

struct PACK {
    u64 ID;
    padding[2];
    u8 Compression_Type;
    padding[3];
    u8 Version;
    u32 CHUNK_Count;
    
    CHUNK chunk[CHUNK_Count];
    CHUNK_Data data[CHUNK_Count];

    
};

enum CompressionType : u8 {
    LZO1X = 0x01,
    LZO2A = 0x02,
    xmemdecompress = 0x03,
    LZO1C = 0x05
};


PACK pack[while(!std::mem::eof())] @0x00;