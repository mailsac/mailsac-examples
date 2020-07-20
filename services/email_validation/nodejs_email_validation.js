const superagent = require('superagent')

superagent
  .get('https://mailsac.com/api/validations/addresses/jimmy@mailsac.com')
  .set('Mailsac-Key', 'YOUR_API_KEY_HERE')
  .then((validation) => {
      console.log(validation.body)
  })
  .catch(err => {
      console.log(err.message)
  })
/*
{
  email: 'jimmy@mailsac.com',
  domain: 'mailsac.com',
  isValidFormat: true,
  local: 'jimmy',
  isDisposable: true,
  disposableDomains: [ 'ledoktre.com', 'mailsac.com', 'totalvista.com', 'slothmail.net' ],
  aliases: [
    'ledoktre.com',   'mailsac.com',
    'totalvista.com', '52.41.136.113',
    'slothmail.net',  'aiwa.fm',
    'tztmax.com',     'cs.msdc.co',
    'zeie.xyz',       'yinpinpin.club',
    'jadeant.top',    'dylans.email',
    'msdc.co'
  ]
}
*/
