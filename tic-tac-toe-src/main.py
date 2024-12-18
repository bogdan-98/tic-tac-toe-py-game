from services.tic_tac_toe_services import TikTakToeServices
from repository.tic_tac_toe_repository import TikTakToeRepository
from ui.consola import Consola
repo = TikTakToeRepository("fisier.txt")
services = TikTakToeServices(repo)
consola = Consola(services)

consola.run()