from models.create_and_patch_model import Addition, CreateAndPatchModel
from models.get_all_params_model import GetAllParamsModel
from models.get_and_delete_model import GetAndDeleteModel
from models.patch_id_model import PatchIdModel


class DataForTests:
    create_entity_body = CreateAndPatchModel(
        addition=Addition(
            additional_info="zaewe5jw4j6bees",
            additional_number=232
        ),
        important_numbers=[15, 2, 24, 15],
        title="aaagechawoo",
        verified=True
    )

    get_all_params = GetAllParamsModel(
        title=None,
        verified=None,
        page=None,
        per_page=None
    )

    delete_entity = GetAndDeleteModel(
        id=24
    )

    get_entity_id = GetAndDeleteModel(
        id=17
    )

    patch_entity_id = PatchIdModel(
        id="12"
    )

    patch_entity_body = CreateAndPatchModel(
        addition=Addition(
            additional_info="eezmena",
            additional_number=111
        ),
        important_numbers=[15, 2, 24, 15],
        title="aaagechawoo",
        verified=True
    )
