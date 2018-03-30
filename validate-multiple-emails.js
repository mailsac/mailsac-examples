const requestp = require('request-promise-native')

const MAILSAC_API_KEY = 'YOUR API KEY GOES HERE';
const addresses = process.argv.slice(2);

requestp.post(`https://mailsac.com/api/validations/addresses`, {
        json: true,
        body: {
            emails: addresses
        },
        headers: {
            'Mailsac-Key': MAILSAC_API_KEY
        },
    })
    .then((results) => {
        console.log(results);
    })
    .catch((err) => {
        console.error('Something broke!', err.message, err.stack);
    });
