const superagent = require('superagent')

superagent
  .post('https://mailsac.com/api/outgoing-messages')
  .set('Mailsac-Key', 'YOUR_API_KEY_HERE')
  .send({
      to: "myfriend@mailsac.com",
      from: "user1@mailsac.com",
      subject: "Hello Myfriend",
      text: "test message from mailsac"
  })
  .then((res) => {
      console.log(res.body)
  })
  .catch(err => {
      console.log(err.message)
  })

  /*
  {
  from: 'user1@mailsac.com',
  to: [ 'myfriend@mailsac.com' ],
  id: 'fe-ipic46bqge8'
}
*/
