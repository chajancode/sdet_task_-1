import random
import factory
from faker import Faker

from models.create_and_patch_model import Addition, CreateAndPatchModel
from models.get_all_params_model import GetAllParamsModel
from models.get_and_delete_model import GetAndDeleteModel
from models.patch_id_model import PatchIdModel


faker = Faker()

MIN_ID, MAX_ID = 1, 50
MIN_PAGE, MAX_PAGE = 1, 10
MIN_NUM, MAX_NUM = 1, 100


class AdditionFactory(factory.Factory):

    class Meta:
        model = Addition

    additional_info = factory.Faker("text", max_nb_chars=12)
    additional_number = factory.Faker(
        "pyint", min_value=MIN_NUM, max_value=MAX_NUM
    )


class CreateAndPatchFactory(factory.Factory):

    class Meta:
        model = CreateAndPatchModel

    addition = factory.SubFactory(AdditionFactory)
    important_numbers = factory.LazyAttribute(
        lambda x: [faker.pyint(MIN_NUM, MAX_NUM) for x in range(3)]
        )
    title = factory.Faker("word")
    verified = factory.LazyAttribute(lambda x: random.choice([True, False]))


class GetAllParamsFactory(factory.Factory):

    class Meta:
        model = GetAllParamsModel

    title = factory.Faker("word")
    verified = factory.LazyAttribute(
        lambda x: random.choice([False, True, None])
    )
    page = factory.Faker("pyint", min_value=MIN_PAGE, max_value=MAX_PAGE)
    per_page = factory.Faker("pyint", min_value=MIN_PAGE, max_value=MAX_PAGE)


class GetAndDeleteFactory(factory.Factory):

    class Meta:
        model = GetAndDeleteModel

    id = factory.Faker("pyint", min_value=MIN_ID, max_value=MAX_ID)


class PatchIdFactory(factory.Factory):

    class Meta:
        model = PatchIdModel

    id = factory.LazyAttribute(lambda x: str(random.randint(1, 51)))
