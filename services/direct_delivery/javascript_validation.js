const request = require('request');

const mailsacKey = 'YOUR_API_KEY_HERE';

const options = {
    url: 'https://mailsac.com/api/addresses/mycustomer@gmail.com/messages',
    headers: {
        'Mailsac-Key': mailsacKey
    }
};

function callback(error, response, body) {
    if (!error && response.statusCode == 200) {
        const info = JSON.parse(body);
        console.log(info);
    }
}

request(options, callback);

// Output from script
[ { _id: '9j1rpnMNc2KbgH9hzk0umIgq-0',
    from: [ [Object] ],
    to: [ [Object] ],
    cc: [],
    bcc: [],
    subject: 'Password reset',
    savedBy: null,
    inbox: 'mycustomer@gmail.com',
    originalInbox: 'mycustomer@gmail.com',
    domain: 'gmail.com',
    received: '2020-07-05T22:25:41.408Z',
    size: 603,
    attachments: [],
    ip: '98.244.15.2',
    via: '172.31.27.141',
    folder: 'inbox',
    labels: [],
    read: null,
    rtls: true,
    links: [ 'https://mywebapp.com/password-reset/PasswordResetToken' ],
    spam: 0.114 } ]
