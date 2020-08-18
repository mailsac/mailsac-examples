const nodemailer = require('nodemailer')

const mailsaUserName = 'MAILSAC_USERNAME'
const mailsacAPIKey = 'MAILSAC_API_KEY'

const transporter = nodemailer.createTransport({
  host: 'capture.mailsac.com',
  port: 5587,
  // will use TLS by upgrading later in the connection with STARTTLS
  secure: false,
  auth: {
    user: mailsaUserName,
    pass: mailsacAPIKey
  }
})

transporter.sendMail({
  from: '"Mywebapp Customer Support" no-reply@mywebapp.com',
  to: 'mycustomer@gmail.com',
  subject: 'Password reset',
  text: `Click on the link to reset you password\r\n
    https://mywebapp.com/password-reset/PasswordResetToken`
})
  .then(response => {
    console.log('Successfully sent mail', response)
  })
  .catch(err => {
    console.log('Failed sending mail', err)
  })

/*
Successfully sent mail {
  accepted: [ 'mycustomer@gmail.com' ],
  rejected: [],
  envelopeTime: 129,
  messageTime: 136,
  messageSize: 413,
  response: '250 OK : queued as 71jiTaUqliiQRb5xMHxja0gU',
  envelope: { from: 'no-reply@mywebapp.com', to: [ 'mycustomer@gmail.com' ] },
  messageId: '<15574d0b-2a51-d854-5755-e2e1b0d29d4f@mywebapp.com>'
}
*/
