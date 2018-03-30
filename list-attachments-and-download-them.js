const fs = require('fs')
const request = require('request');
const requestp = require('request-promise-native')

const MAILSAC_API_KEY = process.env.MAILSAC_KEY || 'YOUR API KEY GOES HERE';
const address = process.argv[2];

if (!address) {
    console.error('Missing email address argument');
    process.exit(1);
}

requestp(`https://mailsac.com/api/addresses/${address}/messages`, {
        json: true,
        headers: {
            'Mailsac-Key': MAILSAC_API_KEY
        },
    })
    .then((messages) => {
        console.log(`fetched ${messages.length} messages for ${address}`);

        messages.forEach((message) => {
            if (!message.attachments) {
                console.log(`${message.subject.substring(0, 10)}... ${message._id} - has no attachments`);
                return
            }
            if (message.attachments) {
                console.log(`${message.subject.substring(0, 10)}... ${message._id} - has ${message.attachments.length} attachments`);
                message.attachments.forEach((checksum) => {
                    const file = fs.createWriteStream(`${checksum}.eml`);
                    request(`https://mailsac.com/api/addresses/${address}/messages/${message._id}/attachments/${checksum}`)
                        .pipe(file);
                });
            }
        });
    })
    .catch((err) => {
        console.error('Something broke!', err.message, err.stack);
    });
