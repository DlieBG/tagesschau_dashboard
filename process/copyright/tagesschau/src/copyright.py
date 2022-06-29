class Copyright:

    def get_copyright(self, imageCopyright):
        
        if 'getty' in imageCopyright.lower():
            return 'Getty Images'
        
        if 'ARD' in imageCopyright or 'NDR' in imageCopyright or 'SWR' in imageCopyright or 'rbb' in imageCopyright:
            return 'ARD'              
        
        if 'AFP' in imageCopyright:
            return 'Agence France-Presse'

        if 'reuters' in imageCopyright.lower():
            return 'Reuters'

        if 'AP' in imageCopyright:
            return 'Associated Press'

        if 'imago' in imageCopyright.lower():
            return 'IMAGO'

        if 'picture alliance' in imageCopyright or 'picture-alliance' in imageCopyright:
            return 'picture alliance'

        if 'dpa' in imageCopyright:
            return 'dpa'

        return 'Freie Journalisten'
