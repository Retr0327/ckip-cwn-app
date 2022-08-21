import pickle
from pathlib import Path


pkg_path = Path("__file__").resolve().parent / "src"
ckip_dir = pkg_path / "models"
ckip_path = ckip_dir / "ckip_drivers.pickle"
has_ckip_path = Path(ckip_path).exists()


def download_ckip_drivers():
    """The download_ckip_drivers function downloads the ckip drivers, and saves
    them to a pickle file if the `ckip_drivers.pickle` does not exist.
    """

    NLP_MODEL = "bert-base"

    if not has_ckip_path:
        from ckip_transformers.nlp import CkipWordSegmenter, CkipPosTagger

        drivers = (CkipWordSegmenter(model=NLP_MODEL), CkipPosTagger(model=NLP_MODEL))

        with open(rf"{ckip_path}", "wb") as file:
            pickle.dump(drivers, file)