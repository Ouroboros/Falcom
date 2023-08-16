import * as path from "path";
import * as utils from "../utils";
import { DirectSound, DirectSoundBuffer } from "./dsound"
import { AT9Decoder, AT9DecodeResult } from "../codec/at9";
import { Modules } from "../modules";

export class VoicePlayer {
    private ptr: NativePointer;
    private ds: DirectSound | undefined;
    private sb: DirectSoundBuffer | undefined;

    constructor(ds: NativePointer) {
        this.ptr = ds;
    }

    loadVoice(voiceId: string): AT9DecodeResult | undefined {
        const idstr = voiceId;

        // ch 001 000 0001
        const voicePath = path.join(Modules.ExePath, 'voice', 'at9', `${idstr.slice(3, 6)}`, `ch${idstr}.at9`);
        const at9 = utils.readFileContent(voicePath);

        if (!at9) {
            console.log(`voice not exists: ${voicePath}`);
            return undefined;
        }

        const ret = AT9Decoder.decode(at9)
        if (!ret)
            return undefined;

        return ret;
    }

    playVoice(voiceId: string, volume: number): number | undefined {
        // console.log('playVoice');
        if (this.ptr.readPointer().isNull())
            return;

        if (this.ds === undefined) {
            this.ds = new DirectSound(this.ptr.readPointer());
        }

        this.stopVoice();

        const voice = this.loadVoice(voiceId);

        if (!voice) {
            console.log('invalid voice id');
            return;
        }

        this.sb = this.ds.CreateSoundBuffer({
            flags       : 0x82,
            bufferBytes : voice.dataSize,
            wfxFormat   : voice.wfxFormat,
        });

        if (!this.sb) {
            console.log('create sb failed');
            return;
        }

        const dsb = this.sb.lock(NULL, ptr(voice.dataSize), 0);

        if (!dsb) {
            console.log('dsb lock failed');
            this.stopVoice();
            return;
        }

        dsb.audioPtr1.writeByteArray(voice.data.readByteArray(dsb.audioBytes1.toInt32())!);
        const audioPtr2 = dsb.audioPtr2;
        if (!audioPtr2.isNull()) {
            audioPtr2.writeByteArray(voice.data.add(dsb.audioBytes1.toUInt32()).readByteArray(dsb.audioBytes2.toUInt32())!);
        }

        this.sb.unlock(dsb);
        this.sb.setVolume(volume);

        this.sb.play(0);

        const bytesPerSec = voice.wfxFormat.add(0x8).readU32();
        const duration = voice.dataSize / bytesPerSec;

        return duration;
    }

    stopVoice() {
        // console.log('stopVoice');
        this.sb?.stop();
        this.sb?.release();
        this.sb = undefined;
    }
}
