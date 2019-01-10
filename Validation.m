function Validation(Data, weights, bias)
    figure
    for a=351:526
        for b=1:6
            sigma(b) = 0;
            for c=1:9
               sigma(b) = Data(a,c)*weights(1,c,b) + sigma(b) + bias(b); 
            end
            hidden(b) = tanh(sigma(b));
        end
        for b=1:2
           sigma(6+b) = 0;
           for c=1:6
              sigma(6+b) = hidden(c)*weights(2,c,b) + bias(6+b); 
           end
           outputs(b) = tanh(sigma(6+b));
           error(6+b) = Data(a,9+b) - outputs(b);
        end
        
        range(a) = a;
        plots(a) = error(8) + error(7);
        plot(range,plots)
        xlim([351,527]);
        ylim([plots(351)-0.1,plots(351)+0.1]);
    end



end