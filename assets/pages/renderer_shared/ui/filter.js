export function applyFilters({
  data = [],
  difficulty = "",
  platform = "",
  os = ""
}) {
  return data.filter((item) => {
    const matchDifficulty =
      !difficulty ||
      item.difficulty === difficulty;

    const matchPlatform =
      !platform ||
      item.platform === platform;

    const matchOS =
      !os ||
      item.os === os;

    return (
      matchDifficulty &&
      matchPlatform &&
      matchOS
    );
  });
}
