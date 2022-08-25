python -c '
import CwnSenseTagger, DistilTag
from CwnGraph import CwnImage

DistilTag.download(upgrade=False)
CwnSenseTagger.download(upgrade=False)
CwnImage.latest()
' | xargs -I {} sh -c 'printf "\e[0;32m{}\e[0;m\n";'


streamlit run ./src/app.py