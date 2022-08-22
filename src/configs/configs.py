import pickle
from pathlib import Path


pkg_path = Path("__file__").resolve().parent / "src"
ckip_dir = pkg_path / "models"
ckip_path = ckip_dir / "ckip_drivers.pickle"


def download_ckip_drivers():
    """The download_ckip_drivers function downloads the ckip drivers, and saves
    them to a pickle file if the `ckip_drivers.pickle` does not exist.
    """

    NLP_MODEL = "bert-base"

    if not Path(ckip_path).exists():
        from ckip_transformers.nlp import (
            CkipWordSegmenter,
            CkipPosTagger,
            CkipNerChunker,
        )

        drivers = (
            CkipWordSegmenter(model=NLP_MODEL),
            CkipPosTagger(model=NLP_MODEL),
            CkipNerChunker(model=NLP_MODEL),
        )

        with open(rf"{ckip_path}", "wb") as file:
            pickle.dump(drivers, file)
