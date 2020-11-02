from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

class UserModel(Model):
    class Meta:
        table_name = 'pynamo-test'
        region = 'ap-northeast-2'
    email = UnicodeAttribute(null=True)
    first_name = UnicodeAttribute(range_key=True)
    last_name = UnicodeAttribute(hash_key=True)


if __name__ == "__main__":
    #UserModel.create_table(read_capacity_units=1, write_capacity_units=1)
    #user = UserModel("John", "Denver")
    #user.email = "djohn@company.org"
    #user.save()
    #for user in UserModel.query("Denver", UserModel.first_name.startswith("J")):
    #    print(user.first_name)
    try:
        user = UserModel.get("John", "Denver")
        print(user)
    except UserModel.DoesNotExist:
        print("User does not exist")