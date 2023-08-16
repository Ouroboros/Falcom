import * as utils from "./utils";

function main() {
    try {
        switch (utils.getGameVersion()) {
            // case 'ed6fc':
            //     import("./ed6fc/ed6fc").then(ed6fc => {
            //         ed6fc.main()
            //     });
            //     break;

            case 'ed6fc_dx9':
                import("./ed6fc_dx9/ed6fc").then(ed6fc_dx9 => {
                    ed6fc_dx9.main();
                });
                break;

            case 'ed6sc_dx9':
                import("./ed6sc_dx9/ed6sc").then(ed6sc_dx9 => {
                    ed6sc_dx9.main();
                });
                break;
        }
    } catch (e) {
        console.log(e);
    }
}

console.log();
main();
