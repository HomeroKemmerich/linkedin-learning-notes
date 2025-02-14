class Settings:
    def __init__(self, output_option='File', language='en_us'):
        self.output_option = output_option
        self.language = language

    #region Getters and setters
    @property
    def input_file(self) -> str:
        return self.__input_file
    
    @input_file.setter
    def input_file(self, value: str):
        self.__input_file = value
    
    @property
    def output_file(self) -> str:
        return self.__output_file
    
    @output_file.setter
    def output_file(self, value: str):
        self.__output_file = value

    @property
    def output_option(self) -> str:
        return self.__output_option
    
    @output_option.setter
    def output_option(self, value: str):
        self.__output_option = value

    @property
    def output_format(self) -> str:
        return self.__output_format
    
    @output_format.setter
    def output_format(self, value: str):
        self.__output_format = value

    @property
    def readwise_api_key(self) -> str:
        return self.__readwise_api_key
    
    @readwise_api_key.setter
    def readwise_api_key(self, value: str):
        self.__readwise_api_key = value

    @property
    def language(self) -> str:
        return self.__language
    
    @language.setter
    def language(self, value: str):
        self.__language = value
    #endregion
