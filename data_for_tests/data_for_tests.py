from utils.data_generators import (
                                    CreateAndPatchFactory,
                                    GetAllParamsFactory,
                                    GetAndDeleteFactory,
                                    PatchIdFactory
                                )


class DataForTests:

    create_entity_body = CreateAndPatchFactory()
    delete_entity = GetAndDeleteFactory()
    get_entity_id = GetAndDeleteFactory()
    patch_entity_id = PatchIdFactory()
    patch_entity_body = CreateAndPatchFactory()
    get_all_params = GetAllParamsFactory()
