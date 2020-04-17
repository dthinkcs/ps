

function main() {
    var option = 0;
    do {

        process.stdin.resume();
        process.stdin.setEncoding('utf-8');

        let inputString = '';
        let currentLine = 0;

        process.stdin.on('data', inputStdin => {
            inputString += inputStdin;
        });

        process.stdin.on('end', _ => {
            inputString = inputString.trim().split('\n').map(string => {
                return string.trim();
            });
            
            main();    
        });

        function readLine() {
            return inputString[currentLine++];
        }

    }while (option != 5);
}

main()