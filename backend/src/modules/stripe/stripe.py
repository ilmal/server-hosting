from flask import Flask, request, jsonify
import requests
import stripe
import random
import string
from game_plans.minecraft_config import get_plan_data

router = Flask(__name__)

def main(request):
    def handle_payment(request):
        # getting the products data


        # putting req data into variables
        data = request.get_json()
        id = data["id"]
        product = data["product"]
        #ref = data["ref"]
        #userID = data["userID"]
        #is_past_server = data["is_past_server"]
        price = get_plan_data.price

        # # ref handler (ref is for referal links)
        # refReturn = None
        # print("REF PRE FUNCTION: ", ref)
        # if ref:
        #     refReturn = refHandler.initialRefCheck(ref)
        #     if refReturn["referal_exist"] and refReturn["discount"] is not None:
        #         price = price * (1 - (refReturn["discount"] / 100))

        # def createServerIDFunc():
        #     result = ""
        #     characters = string.ascii_lowercase
        #     for i in range(19):
        #         result += random.choice(characters)
        #     result += "-" + userID
        #     return result

        try:
            payment = stripe.PaymentIntent.create(
                amount=price,
                currency="EUR",
                #description=f"Referal: {ref}",
                payment_method=id,
                confirm=True
            )
            print("Payment", payment)
            #createUser(payment)
            #refHandler.paymentSuccessRefHandler(payment, ref)

            # user = User.findById(userID)
            # userServerObj = {
            #     "server_id": createServerIDFunc(),
            #     "plan": product["plan"],
            #     "game": product["game"],
            #     "payment_ref": ref,
            #     "payment_id": id,
            #     "date": datetime.datetime.now()
            # }

            # if is_past_server:
            #     for i in range(len(user.servers)):
            #         if user.servers[i]["server_id"] != is_past_server:
            #             continue

            #         serverObj = {
            #             **user.servers[i],
            #             "plan": product["plan"],
            #             "game": product["game"],
            #             "payment_ref": ref,
            #             "payment_id": id,
            #             "date": datetime.datetime.now()
            #         }

            #         user.servers[i] = serverObj
            #         user.past_servers[i] = serverObj

            #         user.save()
            #         return jsonify({
            #             "message": "Payment successful",
            #             "success": True
            #         })

            # user.servers.append(userServerObj)
            # user.past_servers.append(userServerObj)
            # user.save()

            return jsonify({
                "message": "Payment successful",
                "success": True
            })
        except Exception as error:
            print("Error", error)
            return jsonify({
                "message": "Payment failed",
                "success": False
            })
    return handle_payment(request)
        

def get_ref_price():
    refHandlerReturn = refHandler.initialRefCheck(request.get_json()["ref"])
    print("refHandlerReturn.discount", refHandlerReturn)
    if refHandlerReturn["referal_exist"]:
        return jsonify(refHandlerReturn["discount"])
    return jsonify(False)