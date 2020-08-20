const superagent = require('superagent')
const mailsac_api_key = 'YOUR_API_KEY_HERE'

superagent
  .delete('https://mailsac.com/api/addresses/bclinton@mailsac.com/messages/')
  .set('Mailsac-Key', mailsac_api_key)
  .then((res) => {
      console.log(res.status)
  })
  .catch(err => {
      console.error(err.message);
  })

/*
204
*/
