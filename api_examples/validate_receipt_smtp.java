import java.util.HashMap;
import java.util.Map;
import java.util.Properties;
import java.io.IOException;

import javax.mail.Session;
import javax.mail.internet.MimeMessage;
import javax.mail.Transport;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.internet.InternetAddress;

import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;
import com.mashape.unirest.http.exceptions.UnirestException;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.JsonNode;

public class validate_receipt_smtp {

    static String SMTP_USERNAME = "mysmtp_user";
    static String SMTP_PASSWORD = "mysmtp_password";
    static String SMTP_SERVER = "mysmtp_server.company.com";
    static int SMTP_PORT = 587;
    static String FROM_ADDRESS = "myuser@company.com";
    static String FROM_NAME = "MyTest User";
    static String SUBJECT = "Testing email to Mailsac";

    static String API_TOKEN = "MY_API_TOKEN_FROM_MAILSAC";
    static String BASE_URL = "https://mailsac.com/api";

    static String BODY_TEXT = "Mailsac SMTP validate Email Send\r\nThis email was sent using the SMTP to test receipt of an email.";
    
    static void checkReceived(String receiveAddress, String sendAddress, String baseURL, Map<String, String> headers) throws IOException, UnirestException {
        String apiURL = String.format("%s/addresses/%s/messages", baseURL, receiveAddress);
        HttpResponse<String> response = Unirest.get(apiURL)
            .headers(headers)
            .asString();
        ObjectMapper objectMapper = new ObjectMapper();
        Object[] array = objectMapper.readValue(response.getBody(), Object[].class);
        for (int i = 0; i < array.length; i++) {
            JsonNode message = objectMapper.convertValue(array[i], JsonNode.class);
            if (message.get("from").get(0).get("address").toString().contains(sendAddress)) {
                System.out.println(message.get("received"));
            } else {
                System.out.println(String.format("%s has not received an email from %s", receiveAddress, sendAddress));
            }
        }
    }

    public static void main(String[] args) throws IOException, UnirestException, InterruptedException {
        try {
            Properties properties = new Properties();
            properties.setProperty("mail.mime.address.usecanonicalhostname", "false");
            Session session = Session.getInstance(properties);
            MimeMessage message = new MimeMessage(session);
            message.setFrom(new InternetAddress(SMTP_USERNAME));
            message.setSubject(SUBJECT);
            message.setText(BODY_TEXT);
            Transport transport = session.getTransport("smtp");
            transport.connect(SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD);
            for (int i = 1; i < 11; i++) {
                message.addRecipients(Message.RecipientType.TO, InternetAddress.parse(String.format("user%d@mailsac.com", i)));
            }
            message.saveChanges();
            transport.sendMessage(message, message.getAllRecipients());
            System.out.println("Emails sent!");
        } catch (MessagingException e) {
            System.out.println(e);
        }

        Thread.sleep(30);

        for (int i = 1; i < 11; i++) {
            Map<String, String> headers = new HashMap<>();
            headers.put("Mailsac-Key", API_TOKEN);
            checkReceived(String.format("user%d@mailsac.com", i), FROM_ADDRESS, BASE_URL, headers);
        }
    }

}