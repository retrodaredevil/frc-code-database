mkdir -p data/exported
mkdir -p data/raw

cd data/raw
git clone https://github.com/firstwiki/frc0000
git clone https://github.com/firstwiki/frc1000
git clone https://github.com/firstwiki/frc2000
git clone https://github.com/firstwiki/frc3000
git clone https://github.com/firstwiki/frc4000
git clone https://github.com/firstwiki/frc5000
git clone https://github.com/firstwiki/frc6000
git clone https://github.com/firstwiki/frc7000

find frc1000/_frc -name *.md | xargs -I % cp % ../exported
find frc2000/_frc -name *.md | xargs -I % cp % ../exported
find frc3000/_frc -name *.md | xargs -I % cp % ../exported
find frc4000/_frc -name *.md | xargs -I % cp % ../exported
find frc5000/_frc -name *.md | xargs -I % cp % ../exported
find frc6000/_frc -name *.md | xargs -I % cp % ../exported
find frc7000/_frc -name *.md | xargs -I % cp % ../exported

