
#!/bin/bash
mkdir -p $1
cd $1
nextPage="css3-modsel-1.html"
for (( i=1; i <= 172; ++i ))
do
  curl "https://www.w3.org/Style/CSS/Test/CSS3/Selectors/current/html/full/flat/$nextPage" --output "$i.html"
  nextPage="$(cat "$i.html" | grep -o -E "rel=\"next\" .*" | sed -n 's/.*href="\([^"]*\).*/\1/p')"
done
