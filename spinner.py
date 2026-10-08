import time
from halo import Halo

spinner = Halo(
    text="Loading the travel website",
    spinner="dots"
)

spinner.start()
time.sleep(5)
spinner.succeed("Finished!")