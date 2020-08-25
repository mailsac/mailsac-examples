const superagent = require('superagent')

superagent
  .put('https://mailsac.com/api/private-address-forwarding/bclinton@mailsac.com')
  .set('Mailsac-Key', 'YOUR_API_KEY_HERE')
  .send({
      webhook: "https://mywebsite.com/webhooks"
  })
  .then((res) => {
      console.log(res.body)
  })
  .catch(err => {
      console.log(err.message)
  })

  /*
  { _id: 'bclinton@mailsac.com',
  owner: 'mailsac_user',
  forward: null,
  enablews: false,
  webhook: 'https://mywebsite.com/webhooks',
  webhookSlack: null,
  webhookSlackToFrom: null,
  catchAll: null,
  password: null,
  info: '',
  created: '2020-08-19T23:31:15.664Z',
  updated: '2020-08-25T14:04:34.261Z' }
*/
