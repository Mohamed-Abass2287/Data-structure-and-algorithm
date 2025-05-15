from typing import Union, List, Optional


class Artist:
	def __init__(self, real_name : str, stage_name : str, songs: Union[str, List[str]]):
		self.real_name : str = real_name
		self.stage_name : str = stage_name
		self.songs : List[str] = [songs] if isinstance(songs, str) else songs
		self.is_on_stage : bool = False
		self.booked_concerts : List["Concert"] = []

	def call_on_stage(self) -> None:
		if not self.is_on_stage: # If is_on_stage is False
			self.is_on_stage = True
			print(f"The artist {self.stage_name} is now on stage")
		else: # If is_on_stage is True
			print(f"The artist {self.stage_name} is already on stage")

	def perform_song(self, song : Optional[str] = None) -> bool:
			if not self.is_on_stage: # If is_on_stage is False
				print(f"{self.stage_name} needs to be on stage to start performing songs.")
				return False

			if song and song not in self.songs:
				print(f"{self.stage_name} does not know how to perform {song}")
				return False
			
			song_to_perform: str = song if song else self.songs[0]
			print(f"{self.stage_name} is now performing the song {song_to_perform} on stage")
			return True
	
	def remove_from_stage(self) -> None:
		if self.is_on_stage:
			self.is_on_stage = False
			print(f"The artist {self.stage_name} has just been removed from the stage.")
		else:
			print(f"The artist {self.stage_name} is already off the stage.")


bensoul = Artist("Benson Mutua", "Bensoul", ["Navutishwa", "Extra Pressure", "Viva La Vida", "Medicine"])
dj_shiti = Artist("Steve Oduor", "DJ Shitiani", "Nyanya wa Kambo")


dj_shiti.call_on_stage()
dj_shiti.perform_song("Viva La Vida")
dj_shiti.perform_song("Nyanya wa Kambo")

dj_shiti.remove_from_stage()
dj_shiti.remove_from_stage()

bensoul.remove_from_stage()