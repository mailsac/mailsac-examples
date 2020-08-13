curl -s -H "Mailsac-Key: YOUR_API_KEY_HERE" \
    -X GET https://mailsac.com/api/addresses/calendartrinity@mailsac.com/messages \
    | jq .[0]._id | \
    xargs -I {} curl -H "Mailsac-Key: YOUR_API_KEY_HERE" \
    -X GET https://mailsac.com/api/text/calendartrinity@mailsac.com/{}

# curl output
Dogtreats are good!
