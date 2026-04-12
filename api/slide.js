export default async function handler(req, res) {
  try {
    const response = await fetch("https://blaze.bet.br/api/singleplayer-originals/originals/slide_games/recent/history/1");
    const data = await response.json();

    res.status(200).json(data);
  } catch (error) {
    res.status(500).json({ error: "Erro ao buscar dados" });
  }
}
