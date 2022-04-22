import * as utils from "./utils";

function main() {
    switch (utils.getGameVersion()) {
        // case 'ed6fc':
        //     import("./ed6fc/ed6fc").then(ed6fc => {
        //         ed6fc.main()
        //     });
        //     break;

        case 'ed6fc_dx9':
            import("./ed6fc_dx9/ed6fc").then(ed6fc_dx9 => {
                ed6fc_dx9.main()
            });
            break;
    }
}

console.log();
main();
