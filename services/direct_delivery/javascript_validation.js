const superagent = require('superagent')

superagent
  .get('https://mailsac.com/api/addresses/mycustomer@gmail.com/messages')
  .set('Mailsac-Key', 'YOUR_API_KEY_HERE')
  .then((mail) => {
      console.log(mail.body)
  })
  .catch(err => {
      console.log(err.message)
  })

/*
[
  {
    _id: 'ssda77K5zR25P2ErL3Wi8gUnB8-0',
    from: [ [Object] ],
    to: [ [Object] ],
    cc: [],
    bcc: [],
    subject: 'Password reset',
    savedBy: null,
    inbox: 'mycustomer@gmail.com',
    originalInbox: 'mycustomer@gmail.com',
    domain: 'gmail.com',
    received: '2020-07-07T13:52:07.612Z',
    size: 509,
    attachments: [],
    ip: '98.244.15.2',
    via: '172.31.27.141',
    folder: 'inbox',
    labels: [],
    read: null,
    rtls: true,
    links: [ 'https://mywebapp.com/password-reset/PasswordResetToken' ],
    spam: 0.114
  }
]
*/
