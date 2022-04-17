import * as utils from "./utils";

function main() {
    switch (utils.getGameVersion()) {
        case 'ed6fc':
            import("./ed6fc/ed6fc").then(ed6fc => {
                ed6fc.main()
            });
            break;
    }
}

console.log();
main();
