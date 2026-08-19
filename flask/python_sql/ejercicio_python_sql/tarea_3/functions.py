
def format_user(user_record):
        return {
            "id": user_record[0],
            "full_name": user_record[1],
            "email": user_record[2],
            "username":user_record[3],
            "password": user_record[4],
            "date_of_birth": user_record[5],
            "status": user_record[6]
        }