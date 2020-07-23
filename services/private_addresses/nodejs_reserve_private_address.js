const superagent = require('superagent')

superagent
  .post('https://mailsac.com/api/addresses/unitedmonkey@mailsac.com')
  .set('Mailsac-Key', 'YOUR_API_KEY_HERE')
  .then((reservation) => {
      console.log(reservation.body)
  })
  .catch(err => {
      console.log(err.message)
  })
/*
{
  _id: 'unitedmonkey@mailsac.com',
  owner: 'monkeyman',
  forward: null,
  enablews: null,
  webhook: null,
  webhookSlack: null,
  webhookSlackToFrom: null,
  catchAll: null,
  password: null,
  info: '',
  created: '2020-07-23T15:00:00.935Z',
  updated: '2020-07-23T15:00:00.935Z'
}
*/
