const nodemailer = require('nodemailer');

async function main() {
  const transporter = nodemailer.createTransport({
    host: 'in.mailsac.com"',
    port: 587,
    secure: false
  });

  const info = await transporter.sendMail({
    from: '"Mywebapp Customer Support" no-reply@mywebapp.com',
    to: 'mycustomer@gmail.com',
    subject: 'Password reset',
    text: 'Click on the link to reset you password\r\n' +
      'https://mywebapp.com/password-reset/PasswordResetToken'
  });
}
main().catch(console.error);
