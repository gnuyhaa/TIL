const movies = [
  {title: "matrix", isAult: false},
  {title: "kingsman", isAult: true},
  {title: "zootopia", isAult: false}
]
let baby = movies.reduce(function (acc, movie) {
  if (!movie.isAult) {acc.push(`영화제목: ${movie.title}`)}
  return acc
}, [])

console.log(baby)