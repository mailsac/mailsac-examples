const superagent = require('superagent')
const mailsac_api_key = 'YOUR_API_KEY_HERE'
const messageId = 'YOUR_MESSAGE_ID'

superagent
  .delete('https://mailsac.com/api/addresses/bclinton@mailsac.com/messages/' + messageId)
  .set('Mailsac-Key', mailsac_api_key)
  .then((data) => {
      console.log(data.body)
  })
  .catch(err => {
      console.error(err.message);
  })

/*
{
    message: 'Message was deleted.',
    _id: 'sepjrPlPJsJEm6F8_cHeuCAcs-0',
    inbox: 'bclinton@mailsac.com'
}
*/
