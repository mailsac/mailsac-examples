const requestp = require('request-promise-native')

const MAILSAC_API_KEY = 'YOUR API KEY GOES HERE';
const address = process.argv[2];

requestp(`https://mailsac.com/api/validations/addresses/${address}`, {
        json: true,
        headers: {
            'Mailsac-Key': MAILSAC_API_KEY
        },
    })
    .then((results) => {
        console.log(results[0]);
    })
    .catch((err) => {
        console.error('Something broke!', err.message, err.stack);
    });
