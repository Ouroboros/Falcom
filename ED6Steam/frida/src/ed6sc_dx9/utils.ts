export function ED6PseudoCompress(content: ArrayBuffer): ArrayBuffer {
    const BlockSize     = 0x1FFF;
    const ContinueFlag  = 1;
    const StopFlag      = 0;
    let BlockCount      = (content.byteLength / BlockSize) | 0;
    const remaining     = (content.byteLength % BlockSize) | 0;
    const buffer        = Memory.alloc((BlockCount + 2) * 5 + content.byteLength);
    let src             = content.unwrap();
    let dst             = buffer;

    // empty block
    dst.writeU32(0x00200004);
    dst.add(4).writeU8(ContinueFlag);
    dst = dst.add(5);

    while (BlockCount--) {
        /*
            0x1FFF | 0x2000 -> 0xFF3F
            0x1FFF + 4 -> 0x2003
            0xFF3F << 16 | 0x2003 -> 0xFF3F2003
        */
        dst.writeU32(0xFF3F2003);
        dst.add(4).writeByteArray(src.readByteArray(0x1FFF)!);

        src = src.add(BlockSize);
        dst = dst.add(BlockSize + 5);

        dst.sub(1).writeU8(ContinueFlag);
    }

    if (remaining != 0) {
        const tag = ((remaining + 4) | (((remaining >> 8 | (remaining & 0xFF) << 8) | 0x20) << 16)) >>> 0;

        dst.writeU32(tag);
        dst.add(4).writeByteArray(src.readByteArray(remaining)!);
        dst = dst.add(5 + remaining);
    }

    dst.sub(1).writeU8(StopFlag);

    return buffer.readByteArray(dst.sub(buffer).toUInt32())!;
}
