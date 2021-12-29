import * as utils from "./utils";
import { Modules } from "./modules";

export const Addrs = (function() {
    // switch (utils.getGameVersion()) {
    //     case 'ed84_jp':
            return {
                File_Open           : Modules.ED84.base.add(0x0ED240),
                AllocObject         : Modules.ED84.base.add(0x4DAAC0),
                AllocMemory         : Modules.ED84.base.add(0x52E940),
                FreeMemory          : Modules.ED84.base.add(0x52E920),
                Logger_Output       : Modules.ED83.base.add(0x0D6520),
                Logger_Ansi2UTF8    : Modules.ED83.base.add(0x0D4FF0),

                SaveDataChecksum: Modules.ED84.base.add(0x3E4DD0),
            };

        // case 'ed84_us':
        // default:
        //     return {
        //         File_Open   : Modules.ED84.base.add(0),
        //         AllocObject : Modules.ED84.base.add(0),
        //         AllocMemory : Modules.ED84.base.add(0),
        //         FreeMemory  : Modules.ED84.base.add(0),

        //         SaveDataChecksum: Modules.ED84.base.add(0x3E7080),
        //     };
    // }
})();
