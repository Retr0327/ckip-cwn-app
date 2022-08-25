import pickle
from pathlib import Path
from typing import Optional


# --------------------------------------------------------------------
# ckip drivers

pkg_path = Path("__file__").resolve().parent / "src"
ckip_dir = pkg_path / "models"
ckip_path = ckip_dir / "ckip" / "ckip_drivers.pickle"


def download_ckip_drivers():
    """The download_ckip_drivers function downloads the ckip drivers, and saves
    them to a pickle file if the `ckip_drivers.pickle` does not exist.
    """

    NLP_MODEL = "bert-base"

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


# --------------------------------------------------------------------
# cwn packages

cwn_model_path = Path.home().resolve() / ".cwn_graph"


def download_cwn_models(upgrade: Optional[bool] = False):
    import CwnSenseTagger, DistilTag
    from CwnGraph import CwnImage

    DistilTag.download(upgrade=upgrade)
    CwnSenseTagger.download(upgrade=upgrade)
    CwnImage.latest()
