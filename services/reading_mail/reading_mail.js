const superagent = require('superagent')
const mailsac_api_key = 'YOUR_API_KEY_HERE'

superagent
  .get('https://mailsac.com/api/addresses/calendartrinity@mailsac.com/messages')
  .set('Mailsac-Key', mailsac_api_key)
  .then((messages) => {
      messageId = messages.body[0]._id
      superagent
          .get('https://mailsac.com/api/text/calendartrinity@mailsac.com/' + messageId)
          .set('Mailsac-Key', mailsac_api_key)
              .then((messageText) => {
                  console.log(messageText.text)
              })
  })
  .catch(err => {
      console.log(err.message)
  })

/*
Dogtreats are good!
*/
