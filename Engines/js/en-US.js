(function () 
{
    var resultSpeaker = document.querySelector('#resultSpeak');
	var fala;
	
    if (window.SpeechRecognition || window.webkitSpeechRecognition) {

        var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;

        var myRecognition = new SpeechRecognition();

        myRecognition.lang = 'en-US';
		myRecognition.continuous = true;
		myRecognition.interimResults = true;
		
            try {

                myRecognition.start();

            } catch (erro) {
                alert('erro:' + erro.message);
            }
		
		myRecognition.onresult = function(event)
		{
			var interim_transcript = '';
			
			for(var i = event.resultIndex; i < event.results.length; i++)
			{
				if(event.results[i].isFinal)
				{
					var resultSpeak;
					resultSpeak += event.results[i][0].transcript.trim();
					fala = resultSpeak.split('undefined');
					console.log(fala[1]);
					resultSpeaker.innerHTML = fala[1];
				}
				else
				{
					resultSpeaker.innerHTML = 'on';
				}
				
			}
		

		}
		
		myRecognition.onend = function(){
			myRecognition.start();
		}
		
		

        myRecognition.addEventListener('error', function (evt) {

            resultSpeaker.innerHTML = 'error';

        }, false);

    } else {
        resultSpeaker.innerHTML = 'error_suport';
    }

})();
