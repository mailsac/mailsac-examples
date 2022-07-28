const request = require('superagent');
const nodemailer = require('nodemailer');

const checkReceived = (receiveAddress, sendAddress, baseURL, headers) => {
    const apiURL = `${baseURL}/addresses/${receiveAddress}/messages`;
    request
        .get(apiURL)
        .set(headers)
        .then(res => {
            res.body.forEach((message) => {
                if (message.from[0].address == sendAddress) {
                    console.log(message.received)
                } else {
                    console.log(`${receiveAddress} has not received an email from ${sendAddress}`)
                }
            })
        })
        .catch(err => {
            console.log(err.message)
        });
}

const SMTP_USERNAME = 'mysmtp_user';
const SMTP_PASSWORD = 'mysmtp_password';
const SMTP_SERVER = 'mysmtp_server.company.com';
const SMTP_PORT = 587;
const FROM_ADDRESS = 'myuser@company.com';
const FROM_NAME = 'MyTest User';
const SUBJECT = 'Testing email to Mailsac';

const API_TOKEN = 'MY_API_TOKEN_FROM_MAILSAC';
const BASE_URL = 'https://mailsac.com/api';

const BODY_TEXT = "Mailsac SMTP validate Email Send\r\nThis email was sent using the SMTP to test receipt of an email.";

for (let i = 1; i < 11; i++) {
    const transporter = nodemailer.createTransport({
        host: SMTP_SERVER,
        port: SMTP_PORT,
        auth: {
            user: SMTP_USERNAME,
            pass: SMTP_PASSWORD,
        },
    });

    const result = transporter.sendMail({
        from: `"${FROM_NAME}" <${FROM_ADDRESS}>`,
        to: `user${i}@mailsac.com`,
        subject: SUBJECT,
        text: BODY_TEXT,
    }, (err, res) => {
        if (err) {
            console.log(err)
        } else {
            console.log("Email sent!")
        }
    });
}

setTimeout(() => {
    for (let i = 1; i < 11; i++) {
        checkReceived(`user${i}@mailsac.com`, FROM_ADDRESS, BASE_URL, {'Mailsac-Key': API_TOKEN});
    }
}, 30);