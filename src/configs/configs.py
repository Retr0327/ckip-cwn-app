import pickle
from pathlib import Path
from typing import Optional


# --------------------------------------------------------------------
# ckip drivers

pkg_path = Path("__file__").resolve().parent / "src"
ckip_dir = pkg_path / "models"
ckip_path = ckip_dir / "ckip" / "ckip_drivers.pickle"


NLP_MODEL = "bert-base"


def download_ckip_drivers(nlp_model: Optional[str] = NLP_MODEL):
    """The download_ckip_drivers function downloads the ckip drivers, and saves
    them to a pickle file if the `ckip_drivers.pickle` does not exist.
    """

    from ckip_transformers.nlp import (
        CkipWordSegmenter,
        CkipPosTagger,
        CkipNerChunker,
    )

    drivers = (
        CkipWordSegmenter(model=nlp_model),
        CkipPosTagger(model=nlp_model),
        CkipNerChunker(model=nlp_model),
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
