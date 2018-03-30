const requestp = require('request-promise-native');

const MAILSAC_API_KEY = process.env.MAILSAC_KEY || 'YOUR API KEY GOES HERE';
const addresses = process.argv.slice(2);

if (!addresses.length) {
    console.error('Add at least one email address argument');
    process.exit(1);
}

console.log(`validating ${addresses.length} email addresses`);

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
